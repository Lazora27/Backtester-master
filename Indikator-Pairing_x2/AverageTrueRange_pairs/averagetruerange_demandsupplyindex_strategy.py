import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
