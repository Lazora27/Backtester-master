import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
