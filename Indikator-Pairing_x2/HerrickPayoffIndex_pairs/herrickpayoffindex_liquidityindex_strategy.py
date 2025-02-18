import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HerrickPayoffIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HerrickPayoffIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'HerrickPayoffIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
