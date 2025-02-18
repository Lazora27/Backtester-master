import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und TapeReading
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'TapeReading': 1.0
        })
    )
