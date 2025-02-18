import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
