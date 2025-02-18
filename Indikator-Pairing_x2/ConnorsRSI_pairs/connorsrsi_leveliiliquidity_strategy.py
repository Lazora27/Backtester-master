import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
