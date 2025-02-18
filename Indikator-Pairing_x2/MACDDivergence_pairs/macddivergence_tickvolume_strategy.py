import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und TickVolume
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'TickVolume': 1.0
        })
    )
