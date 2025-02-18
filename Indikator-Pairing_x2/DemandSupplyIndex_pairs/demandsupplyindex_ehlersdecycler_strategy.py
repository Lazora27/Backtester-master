import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
