import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'LiquidityIndex': 1.0
        })
    )
