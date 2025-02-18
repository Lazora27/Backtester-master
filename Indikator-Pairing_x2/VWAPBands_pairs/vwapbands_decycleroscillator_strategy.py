import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
