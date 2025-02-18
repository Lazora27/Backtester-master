import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
