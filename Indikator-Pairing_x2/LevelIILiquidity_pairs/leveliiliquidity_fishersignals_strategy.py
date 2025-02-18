import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und FisherSignals
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'FisherSignals': 1.0
        })
    )
