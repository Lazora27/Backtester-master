import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'ProjectionBands': 1.0
        })
    )
