import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und DPOCycles
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'DPOCycles': 1.0
        })
    )
