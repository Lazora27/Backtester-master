import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'GannAngles': 1.0
        })
    )
