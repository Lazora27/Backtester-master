import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_LevelIILiquidity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und LevelIILiquidity
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'LevelIILiquidity': 1.0
        })
    )
