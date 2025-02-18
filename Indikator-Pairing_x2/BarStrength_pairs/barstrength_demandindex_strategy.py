import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und DemandIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'DemandIndex': 1.0
        })
    )
