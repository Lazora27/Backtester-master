import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VerticalHorizontalFilter_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VerticalHorizontalFilter und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'VerticalHorizontalFilter': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
