import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
