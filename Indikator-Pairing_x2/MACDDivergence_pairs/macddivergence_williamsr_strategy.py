import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und WilliamsR
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'WilliamsR': 1.0
        })
    )
