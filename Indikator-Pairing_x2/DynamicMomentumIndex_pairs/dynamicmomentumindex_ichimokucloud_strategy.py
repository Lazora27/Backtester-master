import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
