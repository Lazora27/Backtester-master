import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
