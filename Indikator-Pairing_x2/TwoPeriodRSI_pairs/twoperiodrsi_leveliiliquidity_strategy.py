import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
