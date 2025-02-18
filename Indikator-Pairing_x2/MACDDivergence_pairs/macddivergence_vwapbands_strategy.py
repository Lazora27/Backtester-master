import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'VWAPBands': 1.0
        })
    )
