import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationMomentum_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationMomentum und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'MarketFacilitationMomentum': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
