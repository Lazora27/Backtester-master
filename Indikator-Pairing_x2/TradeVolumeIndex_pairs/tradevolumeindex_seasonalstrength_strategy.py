import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
