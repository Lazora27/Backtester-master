import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
