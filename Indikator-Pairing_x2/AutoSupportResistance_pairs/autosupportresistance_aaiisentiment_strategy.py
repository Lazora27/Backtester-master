import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'AAIISentiment': 1.0
        })
    )
