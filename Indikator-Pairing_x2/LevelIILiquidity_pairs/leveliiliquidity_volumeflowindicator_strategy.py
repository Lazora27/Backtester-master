import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
