import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'EldersForceIndex': 1.0
        })
    )
