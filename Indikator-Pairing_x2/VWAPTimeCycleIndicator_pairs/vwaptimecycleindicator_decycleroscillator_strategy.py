import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPTimeCycleIndicator_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPTimeCycleIndicator und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'VWAPTimeCycleIndicator': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
