import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'KeltnerChannels': 1.0
        })
    )
