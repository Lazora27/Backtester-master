import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
