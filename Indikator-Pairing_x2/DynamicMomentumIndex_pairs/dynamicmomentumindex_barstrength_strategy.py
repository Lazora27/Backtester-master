import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'BarStrength': 1.0
        })
    )
