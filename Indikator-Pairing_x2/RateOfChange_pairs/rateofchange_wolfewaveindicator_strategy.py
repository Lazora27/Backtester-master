import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
