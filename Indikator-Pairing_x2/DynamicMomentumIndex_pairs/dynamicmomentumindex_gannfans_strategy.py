import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und GannFans
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'GannFans': 1.0
        })
    )
