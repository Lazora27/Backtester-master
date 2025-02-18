import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
