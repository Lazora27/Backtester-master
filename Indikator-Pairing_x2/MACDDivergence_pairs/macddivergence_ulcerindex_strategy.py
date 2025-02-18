import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'UlcerIndex': 1.0
        })
    )
