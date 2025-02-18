import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_MarketFacilitationMomentum_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und MarketFacilitationMomentum
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'MarketFacilitationMomentum': 1.0
        })
    )
