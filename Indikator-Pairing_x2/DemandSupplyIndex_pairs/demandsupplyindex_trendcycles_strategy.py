import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
