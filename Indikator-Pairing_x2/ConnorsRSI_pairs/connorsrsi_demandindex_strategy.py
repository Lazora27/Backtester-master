import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DemandIndex': 1.0
        })
    )
