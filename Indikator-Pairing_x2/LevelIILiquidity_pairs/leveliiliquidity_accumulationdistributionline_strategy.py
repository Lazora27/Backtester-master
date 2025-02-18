import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
