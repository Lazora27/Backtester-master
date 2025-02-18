import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'DonchianVolatility': 1.0
        })
    )
