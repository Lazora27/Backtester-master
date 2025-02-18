import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
