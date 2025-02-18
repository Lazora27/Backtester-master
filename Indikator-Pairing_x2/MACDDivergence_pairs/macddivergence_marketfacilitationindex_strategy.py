import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
