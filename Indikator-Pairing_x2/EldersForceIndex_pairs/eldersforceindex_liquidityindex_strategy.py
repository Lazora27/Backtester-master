import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'LiquidityIndex': 1.0
        })
    )
