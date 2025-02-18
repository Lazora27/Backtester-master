import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und DPOCycles
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'DPOCycles': 1.0
        })
    )
