import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
