import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
