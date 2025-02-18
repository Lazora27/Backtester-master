import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'ProjectionBands': 1.0
        })
    )
