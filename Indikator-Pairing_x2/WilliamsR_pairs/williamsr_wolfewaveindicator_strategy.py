import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
