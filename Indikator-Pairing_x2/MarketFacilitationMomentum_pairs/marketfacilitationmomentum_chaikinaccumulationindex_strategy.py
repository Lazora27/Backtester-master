import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationMomentum_ChaikinAccumulationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationMomentum und ChaikinAccumulationIndex
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            },
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            }
        }),
        ('weights', {
            'MarketFacilitationMomentum': 1.0,
            'ChaikinAccumulationIndex': 1.0
        })
    )
