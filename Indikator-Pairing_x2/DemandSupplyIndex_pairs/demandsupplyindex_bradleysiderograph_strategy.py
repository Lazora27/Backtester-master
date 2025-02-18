import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'BradleySiderograph': 1.0
        })
    )
