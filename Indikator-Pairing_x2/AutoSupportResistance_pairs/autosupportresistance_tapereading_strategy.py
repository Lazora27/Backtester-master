import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und TapeReading
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'TapeReading': 1.0
        })
    )
