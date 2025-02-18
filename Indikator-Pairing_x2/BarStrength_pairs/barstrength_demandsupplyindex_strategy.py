import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
